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


// Masque le prix si le status est passager
document.addEventListener('DOMContentLoaded', function () {
    const roleFields = document.querySelectorAll('input[name="role"]');
    const priceField = document.getElementById('id_price');
    const priceFieldWrapper = priceField.closest('div');

    // Fonction pour ajuster le champ prix en fonction du rôle sélectionné
    function adjustPriceField() {
        const isDriverSelected = document.querySelector('input[name="role"]:checked').value === 'Conducteur';
        if (isDriverSelected) {
            // Afficher le champ prix et ne pas modifier sa valeur (laisser l'utilisateur saisir)
            priceFieldWrapper.style.display = 'block';
        } else {
            // Masquer le champ prix et le définir à 0
            priceFieldWrapper.style.display = 'none';
            priceField.value = 0;
        }
    }

    // Écouter les changements sur les champs de rôle
    roleFields.forEach(function (input) {
        input.addEventListener('change', function () {
            adjustPriceField();
        });
    });

    // Initialiser le champ prix lors du chargement de la page
    adjustPriceField();
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