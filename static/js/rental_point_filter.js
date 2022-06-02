function set_cars() {
    $.ajax({
        url: `cars`,
        success: (response) => {
            var option = document.createElement('option')
            option.value = -1
            option.innerHTML = `Izvēlieties automašīnu`
            document.getElementById('cars').appendChild(option)
            response.forEach(element => {
                var option = document.createElement('option')
                option.value = element.rental_point_id
                option.innerHTML = `${element.manufacture} - ${element.model}`
                document.getElementById('cars').appendChild(option)
            })
        },
    });
}

function set_rental_points() {
    $.ajax({
        url: `rental_points`,
        success: (response) => {
            var option = document.createElement('option')
            option.value = -1
            option.innerHTML = `Izvēlieties nomas punktu`
            document.getElementById('rental_point').appendChild(option)
            response.forEach(element => {
                var option = document.createElement('option')
                option.value = element.id
                option.innerHTML = `${element.title}`
                document.getElementById('rental_point').appendChild(option)
            })
        },
    });
}

function filter_cars() {
    document.getElementById('cars').innerHTML = ""
    let id = document.getElementById('rental_point').value
    if (id === "-1") {
        set_cars()
    } 
    else {
        $.ajax({
            url: `rental_point_cars/${id}`,
            success: (response) => {
                response.forEach(element => {
                    var option = document.createElement('option')
                    option.value = element.rental_point_id
                    option.innerHTML = `${element.manufacture} - ${element.model}`
                    document.getElementById('cars').appendChild(option)
                });
            },
        });
    }
}


function filter_rental_points() {
    document.getElementById('rental_point').innerHTML = ""
    let id = document.getElementById('cars').value
    if (id === "-1") {
        set_rental_points()
    } else {
        $.ajax({
            url: `rental_point/${id}`,
            success: (response) => {
                var option = document.createElement('option')
                option.value = response.id
                option.innerHTML = `${response.title}`
                document.getElementById('rental_point').appendChild(option)
                option.disabled = true
            }
        });
    }
}


