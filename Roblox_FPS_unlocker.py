import os
import json
import time

# Set the text color to white and the background to red
os.system("color 4F")


print("Credit to Viper")
print("Note: Make sure to restart your Roblox after doing this.")


time.sleep(2)


os.system("cls")

# Define the path to the Roblox version folder
roblox_path = os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Roblox", "Versions")

# Find the directory containing RobloxPlayerBeta.exe
for version_folder in os.listdir(roblox_path):
    version_path = os.path.join(roblox_path, version_folder)
    if os.path.exists(os.path.join(version_path, "RobloxPlayerBeta.exe")):
        break

# Define the path to the ClientAppSettings.json file
settings_path = os.path.join(version_path, "ClientSettings", "ClientAppSettings.json")

# Check if the ClientSettings folder exists, if not, create it
client_settings_folder = os.path.join(version_path, "ClientSettings")
if not os.path.exists(client_settings_folder):
    os.mkdir(client_settings_folder)


fps_cap = input("Enter the desired FPS cap: ")
if int(fps_cap) > 900:
    print("Error: 900 is the max. Going over the limit may cause crashing.")
    exit()


physics_rate = input("Enter the desired cap for your rendering: ")
if int(physics_rate) > 900:
    print("Error: 900 is the max. Going over the limit may cause issues.")
    exit()

render_rate = input("Enter the desired cap for your physics (MAX 12): ")
if int(render_rate) > 12:
    print("Error: 12 is the max. Going over the limit may cause issues.")
    exit()

# Create the ClientAppSettings.json file with the desired values and additional settings
client_settings = {
    "DFIntTaskSchedulerTargetFps": int(fps_cap),
    "DFIntS2PhysicsSenderRate": int(physics_rate),
    "DFIntDebugDefaultTargetWorldStepsPerFrame": int(render_rate),
    "FFlagHandleAltEnterFullscreenManually": False,
    "FFlagFastGPULightCulling3": True,
    "FFlagPreloadAllFonts": True,
    "FFlagFixGraphicsQuality": True,
    "FFlagAdServiceEnabled": False,
    "DFIntClientLightingTechnologyChangedTelemetryHundredthsPercent": 0,
    "DFStringCrashUploadToBacktraceBaseUrl": "null",
    "DFStringCrashUploadToBacktraceMacPlayerToken": "null",
    "DFStringCrashUploadToBacktraceWindowsPlayerToken": "null",
    "GoogleAnalyticsAccountPropertyID": "null",
    "GoogleAnalyticsAccountPropertyIDPlayer": "null",
    "FStringCoreScriptBacktraceErrorUploadToken": "null",
    "FStringGamesUrlPath": "/games/",
    "DFFlagClientBaseNetworkMetrics": False,
    "DFStringRobloxAnalyticsURL": "null",
    "DFStringTelegrafHTTPTransportUrl": "null",
    "DFStringAltTelegrafHTTPTransportUrl": "null",
    "DFStringTelegrafAddress": "127.0.0.1",
    "DFStringAltTelegrafAddress": "127.0.0.1",
    "DFStringTelemetryV2Url": "null",
    "DFFlagEnableLightstepReporting2": False,
    "DFIntLightstepHTTPTransportHundredthsPercent2": 0,
    "DFStringLightstepHTTPTransportUrlHost": "null",
    "DFStringLightstepHTTPTransportUrlPath": "null",
    "DFStringLightstepToken": "null",
    "FFlagDebugDisableTelemetryEphemeralCounter": True,
    "FFlagDebugDisableTelemetryEphemeralStat": True,
    "FFlagDebugDisableTelemetryEventIngest": True,
    "FFlagDebugDisableTelemetryPoint": True,
    "FFlagDebugDisableTelemetryV2Counter": True,
    "FFlagDebugDisableTelemetryV2Event": True,
    "FFlagDebugDisableTelemetryV2Stat": True,
    "DFStringHttpPointsReporterUrl": "null",
    "DFStringAltHttpPointsReporterUrl": "null",
    "DFStringAnalyticsEventStreamUrlEndpoint": "null"
    # Add other settings here
}

# Write settings to JSON file
with open(settings_path, "w") as settings_file:
    json.dump(client_settings, settings_file, indent=4)


with open(os.path.join(version_path, "secretsettings.txt"), "w") as secret_file:
    secret_file.write("PhysicsRate=540")


loading = "Loading "
hashes = "####################"
for i in range(1, 21):
    os.system("cls")
    print(loading + hashes[:i])
    time.sleep(0.1)

print(f"FPS cap has been set to {fps_cap}, RENDER set to {physics_rate}, PHYSICS has also been set to {render_rate}.")
input("Press Enter to exit...")
