flatpickr(".flatpickr", {
    dateFormat: "d/m/Y",
    minDate: "today",
});

// masquer ou afficher les champs de date et d'heure de retour en fonction de l'état
document.addEventListener('DOMContentLoaded', function () {
    const statusField = document.querySelector('input[name="status"]:checked');
    const endDateField = document.getElementById('id_end_date');
    const endTimeField = document.getElementById('id_end_time');

    // Fonction pour masquer/afficher les champs de retour
    function toggleReturnFields() {
        const isRoundTrip = document.querySelector('input[name="status"]:checked').value === 'Aller-Retour';
        if (endDateField && endTimeField) {
            endDateField.closest('div').style.display = isRoundTrip ? 'block' : 'none';
            endTimeField.closest('div').style.display = isRoundTrip ? 'block' : 'none';
        }
    }

    // Écouter les changements sur le champ de statut
    document.querySelectorAll('input[name="status"]').forEach(function (input) {
        input.addEventListener('change', function () {
            toggleReturnFields();
        });
    });

    // Initialiser les champs lors du chargement de la page
    toggleReturnFields();
});


// Masque les infos de retour si le voyage est simple
document.addEventListener("DOMContentLoaded", function() {
    const returnTripCheckbox = document.getElementById('id_return_trip');
    const returnSection = document.getElementById('return_section');

    // Masquer la section de retour par défaut
    returnSection.style.display = 'none';

    // Ajouter un événement de changement au checkbox
    returnTripCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // Si coché, afficher la section de retour
            returnSection.style.display = 'block';
        } else {
            // Si décoché, masquer la section de retour
            returnSection.style.display = 'none';
        }
    });
});

// Masquer les jours de la semaine
document.addEventListener("DOMContentLoaded", function() {
    const regularRadio = document.getElementById('id_trip_type_0'); // assuming 'Régulier' is the first radio button
    const punctualRadio = document.getElementById('id_trip_type_1'); // assuming 'Ponctuel' is the second radio button
    const weekdaysSection = document.getElementById('weekdays_section');

    // Masquer la section des jours par défaut
    weekdaysSection.style.display = 'none';

    // Ajouter des écouteurs d'événements pour afficher/masquer la section des jours
    regularRadio.addEventListener('change', function() {
        if (this.checked) {
            weekdaysSection.style.display = 'block';
        }
    });

    punctualRadio.addEventListener('change', function() {
        if (this.checked) {
            weekdaysSection.style.display = 'none';
        }
    });
});


//

$(document).ready(function() {
  $('#afficherNumero').click(function() {
    // Récupérer le numéro de téléphone réel depuis l'attribut data-phone
    var numeroReel = $(this).data('phone');

    // Remplacer le contenu du bouton par le vrai numéro
    $(this).text(numeroReel);
  });
});