# DSC Interval Camera (Android)

A native Android Camera2 interval-photo app that takes photos automatically while a laptop displays timed pages.

**Controls:** initial delay (seconds until first photo), interval between photos, number of photos, START and STOP. **Zoom v1.1:** 0.6× requested by default where supported; 0.6×, 1×, 2× buttons and slider. The screen reports the true minimum if Android hides the ultrawide lens. Zoom affects preview and saved JPEGs. Photos remain on the phone under `Pictures/DSCIntervalCamera`. No upload or network access.

**Download APK:** Open the [Actions tab](https://github.com/arrow2851/Camera_capture/actions/workflows/build-apk.yml), open the latest successful `Build installable APK` run, and download the `DSC-Interval-Camera-debug-APK` artifact. Extract its ZIP to get `app-debug.apk`.

**Source:** This repository stores the v1.0 Android base project as `android-source.tar.xz` and the v1.1 camera update as `zoom-change.patch.xz`. GitHub Actions extracts the base, applies the patch, then builds the APK. To inspect locally, run `tar -xJf android-source.tar.xz` from a new empty directory.

**Build:** Java 17, Gradle 8.9, Android SDK 35, Android Gradle Plugin 8.7.3. For manual builds, extract the source archive then run `gradle assembleDebug`.

**Recommended 3-photo test:** Initial delay 4s, interval 8s, photo count 3. Start the Python laptop slideshow at the same time you press START in the app.

Only the generic camera application source is in this repository. Do not commit proprietary code or captured photos.

**Status:** Build and phone camera functionality must be verified; a CI-successful APK only confirms compilation, not camera behavior on every device.
