cd ..\usplat\00000004.app
del savedata_ja.arc
del savedata_ja.arc.ash
wszst CREATE savedata_ja -a -v -d savedata_ja.arc
ashcompress savedata_ja.arc
del savedata_ja.arc
cd ..\00000005.app
for /d %%i in (.\*) do (
    cd %%~nxi
    del l10n_ui.arc
    del man.brres
    del msg.arc
    del esrborn.arc
    del l10n_ui.arc.ash
    del man.brres.ash
    del msg.arc.ash
    del esrborn.arc.ash
    wszst CREATE l10n_ui -a -v -d l10n_ui.arc
    ashcompress l10n_ui.arc
    del l10n_ui.arc
    wszst CREATE man -a -v
    ashcompress man.brres
    del man.brres
    wszst CREATE msg -a -v -d msg.arc
    ashcompress msg.arc
    del msg.arc
    wszst CREATE esrborn -a -v -d esrborn.arc
    ashcompress esrborn.arc
    del esrborn.arc
    cd ..
)
