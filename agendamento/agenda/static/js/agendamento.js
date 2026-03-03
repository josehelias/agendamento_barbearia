const selectServico = document.querySelector('#barbeiro-select');
selectServico.addEventListener('change', function() {
    const barbeiroId = this.value;
    const data = document.getElementById('id_data').value;
    alert('Data selecionada: ' + data);
    const container = document.getElementById('grid-horarios');

    if (!data) {
        container.innerHTML = "Selecione uma data primeiro.";
        return;
    }

    container.innerHTML = "Carregando horários...";

    fetch(`/buscar-horarios/?barbeiro_id=${barbeiroId}&data=${data}`)
        .then(response => response.json())
        .then(data => {
            container.innerHTML = "";

            if (data.horarios.length === 0) {
                container.innerHTML = "";
                return;
            }

            let html = `
                <label for="id_hora">Selecione um horário:</label>
                <select id="id_hora" name="hora" required class="form-select mt-2">
            `;

            data.horarios.forEach(hora => {
                html += `<option value="${hora}">${hora}</option>`;
            });

            html += `</select>`;

            container.innerHTML = html;

        })
        .catch(() => {
            container.innerHTML = "Erro ao carregar horários.";
        });
});
