cd ..\usplat\00000005.app
for /d %%i in (.\*) do (
    cd %%~nxi
    mogrify l10n_ui\arc\timg\*.png
    cd ..
)
