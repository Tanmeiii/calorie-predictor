document.addEventListener(
    "DOMContentLoaded",
    function () {

        const height =
            document.getElementById(
                "height"
            );

        const weight =
            document.getElementById(
                "weight"
            );

        const bmi =
            document.getElementById(
                "bmi"
            );

        function calculateBMI() {

            const h =
                parseFloat(
                    height.value
                );

            const w =
                parseFloat(
                    weight.value
                );

            if (!h || !w) {

                bmi.value = "";

                return;
            }

            const heightMeters =
                h / 100;

            const bmiValue =
                w /
                (
                    heightMeters *
                    heightMeters
                );

            bmi.value =
                bmiValue.toFixed(2);
        }

        height.addEventListener(
            "input",
            calculateBMI
        );

        weight.addEventListener(
            "input",
            calculateBMI
        );

    }
);