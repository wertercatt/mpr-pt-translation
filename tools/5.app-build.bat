cd 00000005
for /d %%i in (.\*) do (
    cd %%~nxi
    wszst CREATE l10n_ui -a -v -d l10n_ui.arc
    wszst CREATE man -a -v
    wszst CREATE msg -a -v -d msg.arc
    wszst CREATE esrborn -a -v -d esrborn.arc
    cd ..
)
