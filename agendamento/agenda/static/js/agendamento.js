document.querySelectorAll('.radio-barbeiro').forEach(radio => {
    radio.addEventListener('change', function(){
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
                    container.innerHTML = "<p>Sem horários disponíveis.</p>";
                    return;
                }

                data.horarios.forEach(hora => {
                    container.innerHTML += `
                        <label class="btn-hora">
                            <input type="radio" name="hora" value="${hora}">
                            <span>${hora}</span>
                        </label>
                    `;
                });
            })
            .catch(() => {
                container.innerHTML = "Erro ao carregar horários.";
            });
    });
});
