flatpickr(".flatpickr", {
    dateFormat: "Y-d-m",
    minDate: "today"
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
    const priceFieldWrapper = document.getElementById('id_price').closest('div');

    // Fonction pour masquer/afficher le champ prix
    function togglePriceField() {
        const isDriverSelected = document.querySelector('input[name="role"]:checked').value === 'Conducteur';
        priceFieldWrapper.style.display = isDriverSelected ? 'block' : 'none';
    }

    // Écouter les changements sur les champs de rôle
    roleFields.forEach(function (input) {
        input.addEventListener('change', function () {
            togglePriceField();
        });
    });

    // Initialiser le champ prix lors du chargement de la page
    togglePriceField();
});

//

