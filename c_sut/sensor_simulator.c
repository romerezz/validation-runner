#include <stdio.h>
#include <string.h>

typedef enum {
    SENSOR_MODE_NORMAL,
    SENSOR_MODE_HIGH_TEMPATURE,
    SENSOR_MODE_LOW_VOLTAGE,
    SENSOR_MODE_HIGH_CURRENT,
    SENSOR_MODE_INVALID
} SensorMode;

typedef struct {
    double temperature;
    double voltage;
    int current;
} SensorTelemetry;

SensorMode parse_sensor_mode(char *mode_text);
SensorTelemetry generate_telemetry(SensorMode mode);
void print_telemetry(SensorTelemetry telemetry);

int main(int argc, char *argv[])
{
    if (argc != 3 || strcmp(argv[1], "--mode") != 0) {
        return 1;
    }

    SensorMode mode = parse_sensor_mode(argv[2]);

    if (mode == SENSOR_MODE_INVALID) {
        return 1;
    } 

    SensorTelemetry telemetry = generate_telemetry(mode);
    print_telemetry(telemetry);

    return 0;
}

SensorMode parse_sensor_mode(char *mode_text) {
    if (strcmp(mode_text, "normal") == 0) return SENSOR_MODE_NORMAL;
    if (strcmp(mode_text, "high_tempature") == 0) return SENSOR_MODE_HIGH_TEMPATURE;
    if (strcmp(mode_text, "low_voltage") == 0) return SENSOR_MODE_LOW_VOLTAGE;
    if (strcmp(mode_text, "high_current") == 0) return SENSOR_MODE_HIGH_CURRENT;
    return SENSOR_MODE_INVALID;
}

SensorTelemetry generate_telemetry(SensorMode mode) {
    SensorTelemetry telemtry;

    if (mode == SENSOR_MODE_NORMAL) {
        telemtry.temperature = 45.5;
        telemtry.voltage = 5.4;
        telemtry.current = 1;
    }
    
    return telemtry;
}

void print_telemetry(SensorTelemetry telemetry) {
    printf(
    "TEMPERATURE=%.1f\n"
    "VOLTAGE=%.1f\n"
    "CURRENT=%d\n",
    telemetry.temperature,
    telemetry.voltage,
    telemetry.current
    );
}