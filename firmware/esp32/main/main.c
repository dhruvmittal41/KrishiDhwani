/* ESP-IDF scaffold only. No microphone capture or Wi-Fi upload yet. */
#include "esp_log.h"
void app_main(void) {
    ESP_LOGI("krishidhwani", "Scaffold: configure board, I2S microphone and upload pipeline");
    /* TODO: I2S capture -> basic filtering -> bounded clip buffer -> HTTP upload.
       Never classify insect sounds here; classification belongs on the Pi. */
}
