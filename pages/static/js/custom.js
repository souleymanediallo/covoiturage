flatpickr(".flatpickr", {
    dateFormat: "Y-d-m",
    minDate: "today"
});

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

$(document).ready(function () {
    $('input[type="radio"][name="trip_type"]').change(function() {
        if ($(this).val() === 'Aller Retour') {
            $('#returnDateSection').show();
            $('#returnTimeSection').show();
        } else {
            $('#returnDateSection').hide();
            $('#returnTimeSection').hide();
        }
    });

    // Initialisez l'état si "Aller Retour" est déjà sélectionné
    if ($('input[type="radio"][name="trip_type"]:checked').val() === 'Aller Retour') {
        $('#returnDateSection').show();
        $('#returnTimeSection').show();
    }
});