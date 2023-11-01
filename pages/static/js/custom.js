
$(document).ready(function () {
    $("#increase-price").click(function () {
        var currentPrice = parseInt($("#price").val());
        currentPrice += 500;
        $("#price").val(currentPrice);
    });

    $("#decrease-price").click(function () {
        var currentPrice = parseInt($("#price").val());
        currentPrice = Math.max(0, currentPrice - 500);
        $("#price").val(currentPrice);
    });
});


$(document).ready(function () {
    $("#increase-seat_go").click(function () {
        var currentSeat_go = parseInt($("#seat_go").val());
        currentSeat_go = Math.min(9, currentSeat_go + 1);
        $("#seat_go").val(currentSeat_go);
    });

    $("#decrease-seat_go").click(function () {
        var currentSeat_go = parseInt($("#seat_go").val());
        currentSeat_go = Math.max(1, currentSeat_go - 1);
        $("#seat_go").val(currentSeat_go);
    });
});

$(document).ready(function () {
    $("#increase-luggage").click(function () {
        var currentLuggage = parseInt($("#luggage").val());
        currentLuggage = Math.min(20, currentLuggage + 1);
        $("#luggage").val(currentLuggage);
    });

    $("#decrease-luggage").click(function () {
        var currentLuggage = parseInt($("#luggage").val());
        currentLuggage = Math.max(0, currentLuggage - 1);
        $("#luggage").val(currentLuggage);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const tripTypeField = document.getElementById("trip_type");
    const dateRetourField = document.getElementById("date_retour_field");

    // Function to toggle the visibility of the "Date de retour" field
    function toggleDateRetourField() {
        if (tripTypeField.value === "Aller Retour") {
            dateRetourField.style.display = "block";
        } else {
            dateRetourField.style.display = "none";
        }
    }

    // Initial toggle based on default value
    toggleDateRetourField();

    // Add event listener to the "Type de trajet" field
    tripTypeField.addEventListener("change", toggleDateRetourField);
});