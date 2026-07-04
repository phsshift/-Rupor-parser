[app]
title = Rupor Events
package.name = ruporevents
package.domain = org.phase.shift
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,md
version = 0.1
requirements = python3,kivy,requests,beautifulsoup4,certifi,urllib3,idna,charset-normalizer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 35
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.gradle_dependencies = 
android.add_gradle_repositories = 
android.enable_androidx = True
p4a.branch = develop
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1
