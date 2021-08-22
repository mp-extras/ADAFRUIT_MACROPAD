/*
 * Copyright (c) 2021 Mark Grosen <mark@grosen.org>
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

// -----------------------------------------------------
// NOTE: THIS HEADER IS ALSO INCLUDED BY ASSEMBLER SO
//       SHOULD ONLY CONSIST OF PREPROCESSOR DIRECTIVES
// -----------------------------------------------------

#ifndef _BOARDS_ADAFRUIT_MACROPAD_H
#define _BOARDS_ADAFRUIT_MACROPAD_H

// For board detection
#define ADAFRUIT_MACROPAD

// On some samples, the xosc can take longer to stabilize than is usual
#ifndef PICO_XOSC_STARTUP_DELAY_MULTIPLIER
#define PICO_XOSC_STARTUP_DELAY_MULTIPLIER 64
#endif

//------------- LED -------------//
// No normal LED
// #define PICO_DEFAULT_LED_PIN 13

#ifndef PICO_DEFAULT_WS2812_PIN
#define PICO_DEFAULT_WS2812_PIN 19
#endif

//------------- I2C -------------//
#ifndef PICO_DEFAULT_I2C
#define PICO_DEFAULT_I2C 0
#endif

#ifndef PICO_DEFAULT_I2C_SDA_PIN
#define PICO_DEFAULT_I2C_SDA_PIN 20
#endif

#ifndef PICO_DEFAULT_I2C_SCL_PIN
#define PICO_DEFAULT_I2C_SCL_PIN 21
#endif

//------------- SPI -------------//
#ifndef PICO_DEFAULT_SPI
#define PICO_DEFAULT_SPI 1
#endif

#ifndef PICO_DEFAULT_SPI_TX_PIN
#define PICO_DEFAULT_SPI_TX_PIN 27
#endif

#ifndef PICO_DEFAULT_SPI_RX_PIN
#define PICO_DEFAULT_SPI_RX_PIN 28
#endif

#ifndef PICO_DEFAULT_SPI_SCK_PIN
#define PICO_DEFAULT_SPI_SCK_PIN 26
#endif

//------------- FLASH -------------//

#define PICO_BOOT_STAGE2_CHOOSE_W25Q080 1

#ifndef PICO_FLASH_SPI_CLKDIV
#define PICO_FLASH_SPI_CLKDIV 2
#endif

#ifndef PICO_FLASH_SIZE_BYTES
#define PICO_FLASH_SIZE_BYTES (8 * 1024 * 1024)
#endif

// All boards have B1 RP2040
#ifndef PICO_FLOAT_SUPPORT_ROM_V1
#define PICO_FLOAT_SUPPORT_ROM_V1 0
#endif

#ifndef PICO_DOUBLE_SUPPORT_ROM_V1
#define PICO_DOUBLE_SUPPORT_ROM_V1 0
#endif

#endif
