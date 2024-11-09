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


// Fonction pour afficher le numéro de téléphone réel
$(document).ready(function() {
  $('#afficherNumero').click(function() {
    // Récupérer le numéro de téléphone réel depuis l'attribut data-phone
    var numeroReel = $(this).data('phone');

    // Remplacer le contenu du bouton par le vrai numéro
    $(this).text(numeroReel);
  });
});