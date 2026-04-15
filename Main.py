import pykraken as kn

kn.init()
kn.window.create("Kraken Example", 900, 500)

while kn.window.is_open():
    kn.event.poll()

    kn.renderer.present()

kn.quit()