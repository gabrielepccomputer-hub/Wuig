[Setup]
AppName=Salsicciotto Dash
AppVersion=1.0
AppPublisher=Open Source Community
DefaultDirName={autopf}\SalsicciottoDash
DefaultGroupName=Salsicciotto Dash
OutputDir=installer_output
OutputBaseFilename=SalsicciottoDash_Setup
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "italian"; MessagesFile: "compiler:Languages/Italian.isl"

[Files]
Source: "dist\SalsicciottoDash.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Salsicciotto Dash"; Filename: "{app}\SalsicciottoDash.exe"
Name: "{autodesktop}\Salsicciotto Dash"; Filename: "{app}\SalsicciottoDash.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crea un'icona sul Desktop"; GroupDescription: "Collegamenti aggiuntivi:"

[Run]
Filename: "{app}\SalsicciottoDash.exe"; Description: "Avvia Salsicciotto Dash"; Flags: nowait postinstall skipifsilent
