all:
	make -C $(MICROPYTHON)/ports/rp2hid BOARD_DIR=$(PWD) BOARD=ADAFRUIT_MACROPAD

deploy:
	cp $(MICROPYTHON)/ports/rp2hid/build-ADAFRUIT_MACROPAD/rp2hid.uf2 /media/$USER/RPI-RP2

clean:
	make -C $(MICROPYTHON)/ports/rp2hid BOARD_DIR=$(PWD) BOARD=ADAFRUIT_MACROPAD clean
