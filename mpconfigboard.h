#define MICROPY_HW_BOARD_NAME "Adafruit MacroPad"
#define MICROPY_HW_FLASH_STORAGE_BYTES (7 * 1024 * 1024)

#define MICROPY_HW_USB_VID (0x2e8a)
#define MICROPY_HW_USB_PID (0x8109)

// STEMMA QT / Qwiic on I2C0
#define MICROPY_HW_I2C0_SCL (21)
#define MICROPY_HW_I2C0_SDA (20)

// SPI1 for SH1106 OLED Dispaly
#define MICROPY_HW_SPI1_SCK (26)
#define MICROPY_HW_SPI1_MOSI (27)
#define MICROPY_HW_SPI1_MISO (28)

// GPIO19 - Neopixel
// GPIO12 - Button (and BOOT)

// user's choice
#define MICROPY_REPL_EMACS_KEYS (1)
