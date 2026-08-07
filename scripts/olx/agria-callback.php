<?php
/**
 * OLX Partner API — callback OAuth2 dla aplikacji „Agria.pl" (client_id 203091).
 * Redirect URI zarejestrowany w developer.olx.pl: https://auratest.pl/olx/agria-callback.php
 *
 * Kod autoryzacyjny OLX żyje 60 s, więc wymiana na tokeny leci od razu tutaj.
 * Sekrety i tokeny trzymane poza web-rootem w ~/secrets/olx/.
 */

const AGRIA_OLX_SECRETS = '/home/host476470/domains/auratest.pl/olx-private/';
const AGRIA_OLX_TOKEN_URL = 'https://www.olx.pl/api/open/oauth/token';
const AGRIA_OLX_REDIRECT_URI = 'https://auratest.pl/olx/agria-callback.php';

header('Content-Type: text/plain; charset=utf-8');

function agria_olx_die(string $msg, int $code = 400): void {
    http_response_code($code);
    echo $msg . "\n";
    exit;
}

function agria_olx_env(): array {
    $path = AGRIA_OLX_SECRETS . 'agria-app.env';
    if (!is_readable($path)) {
        agria_olx_die('BLAD: brak agria-app.env', 500);
    }
    $env = [];
    foreach (file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
        if ($line === '' || $line[0] === '#' || !str_contains($line, '=')) {
            continue;
        }
        [$k, $v] = explode('=', $line, 2);
        $env[trim($k)] = trim($v, " \t\"'");
    }
    return $env;
}

$code  = $_GET['code']  ?? '';
$state = $_GET['state'] ?? '';

if (isset($_GET['error'])) {
    agria_olx_die('OLX odmowil autoryzacji: ' . $_GET['error'] . ' — ' . ($_GET['error_description'] ?? ''));
}
if ($code === '') {
    agria_olx_die('BLAD: brak parametru code (ten adres jest wywolywany przez OLX, nie recznie).');
}

// state jednorazowy — zapisany przez ~/bin/olx-agria url, chroni endpoint przed obcym wywolaniem
$statePath = AGRIA_OLX_SECRETS . 'agria-state.txt';
$expected  = is_readable($statePath) ? trim((string) file_get_contents($statePath)) : '';
if ($expected === '' || !hash_equals($expected, $state)) {
    agria_olx_die('BLAD: nieprawidlowy state — uruchom flow od nowa przez ~/bin/olx-agria url', 403);
}
@unlink($statePath);

$env = agria_olx_env();

$ch = curl_init(AGRIA_OLX_TOKEN_URL);
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 30,
    CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
    CURLOPT_POSTFIELDS     => json_encode([
        'grant_type'    => 'authorization_code',
        'client_id'     => $env['OLX_CLIENT_ID'] ?? '',
        'client_secret' => $env['OLX_CLIENT_SECRET'] ?? '',
        'code'          => $code,
        'scope'         => $env['OLX_SCOPE'] ?? 'v2 read write',
        'redirect_uri'  => AGRIA_OLX_REDIRECT_URI,
    ]),
]);
$body   = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err    = curl_error($ch);
curl_close($ch);

if ($body === false) {
    agria_olx_die('BLAD curl: ' . $err, 502);
}

$data = json_decode($body, true);
if ($status !== 200 || !isset($data['access_token'])) {
    agria_olx_die("BLAD wymiany kodu (HTTP $status):\n" . $body, 502);
}

$data['obtained_at'] = time();
$data['expires_at']  = time() + (int) ($data['expires_in'] ?? 0);

$tokenPath = AGRIA_OLX_SECRETS . 'agria-tokens.json';
file_put_contents($tokenPath, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
chmod($tokenPath, 0600);

echo "OK — tokeny zapisane.\n";
echo 'scope: ' . ($data['scope'] ?? '?') . "\n";
echo 'access_token wygasa: ' . date('Y-m-d H:i:s', $data['expires_at']) . "\n";
echo 'refresh_token: ' . (isset($data['refresh_token']) ? 'jest' : 'BRAK') . "\n";
