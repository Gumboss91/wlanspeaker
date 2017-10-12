# wlanspeaker

Autoload:
unter /etc/rc.local die Zeile Hinzufügen
  python /home/pi/wlanspeaker/WlanSpeakerServer.py

Musik wird per sftp auf den Raspberry Pi geladen unte /home/pi/Music/
netzwerkname: tapFXspeaker

Komandos per UDP auf Port 5005

  load <dateiname.endung>
  play
  playn <anzahl der Widerholungen>
  plaloop
  pause
  unpause
  stop
  volumen <float mit punk zwischen 0 und 1>

