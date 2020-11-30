
$(document).ready(function () {
    var last_index = 0

    const interval_ms = 1000
    setInterval(function () {
        const sensor_ids = [0, 1]

        sensor_ids.forEach(function (sensor_id, index) {
            const sensor_id_str = (sensor_id +1).toString()

            GetSensorDataLast(USER_ID, sensor_id,
                function () {
                    const dataframe = JSON.parse(this.responseText)
                    //console.log(dataframe)
                    for (datarow of dataframe) {

                        const ambient_temperature = datarow.ambiente_temperature + ' °C'
                        const internal_temperature = datarow.internal_temperature + ' °C'
                        const voltage = datarow.voltage + ' V'
                        const current = datarow.current + ' A'
                        const status = datarow.status + ''

                        updateValue("freezer_" + sensor_id_str + "_ambient_temperature", ambient_temperature)
                        updateValue("freezer_" + sensor_id_str + "_internal_temperature", internal_temperature)
                        updateValue("freezer_" + sensor_id_str + "_status", status)
                        updateValue("freezer_" + sensor_id_str + "_voltage", voltage)
                        updateValue("freezer_" + sensor_id_str + "_current", current)

                        last_index += 1
                    }
                }
            )

        })

    }, interval_ms);

});
