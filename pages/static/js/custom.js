flatpickr(".flatpickr", {
    dateFormat: "d/m/Y",
    minDate: "today",
});

flatpickr("#id_start_time",{
    enableTime: true,
    noCalendar: true,  // Désactive l'affichage du calendrier
    dateFormat: "H:i",  // Format d'affichage de l'heure
    time_24hr: true  // Utilise le format 24 heures
});

flatpickr("#id_return_time",{
    enableTime: true,
    noCalendar: true,  // Désactive l'affichage du calendrier
    dateFormat: "H:i",  // Format d'affichage de l'heure
    time_24hr: true  // Utilise le format 24 heures
});

flatpickr(".time-covoiturage", {
    enableTime: true,
    noCalendar: true,  // Désactive l'affichage du calendrier
    dateFormat: "H:i",  // Format d'affichage de l'heure
    time_24hr: true  // Utilise le format 24 heures
});


// Afficher ou masquer les champs de l'aller-retour en fonction de l'option sélectionnée
document.addEventListener('DOMContentLoaded', function() {
    const tripTypeInputs = document.querySelectorAll('input[name="trip_type"]');
    const roundTripFields = document.getElementById('roundTripFields');

    tripTypeInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value === 'round_trip') {  // Assurez-vous que cette valeur correspond à l'option "aller-retour"
                roundTripFields.style.display = 'flex';
            } else {
                roundTripFields.style.display = 'none';
            }
        });
    });

    // Masquer au chargement initial si "aller simple" est sélectionné par défaut
    const selectedTripType = document.querySelector('input[name="trip_type"]:checked');
    if (selectedTripType && selectedTripType.value !== 'round_trip') {
        roundTripFields.style.display = 'none';
    }
});


// Fonction pour afficher le numéro de téléphone réel
$(document).ready(function() {
  $('#afficherNumero').click(function() {
    // Récupérer le numéro de téléphone réel depuis l'attribut data-phone
    var numeroReel = $(this).data('phone');

    // Remplacer le contenu du bouton par le vrai numéro
    $(this).text(numeroReel);
  });
});