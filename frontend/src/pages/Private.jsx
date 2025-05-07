import React, { useEffect, useState } from "react";

export const Private = () => {
    const [message, setMessage] = useState("");

    useEffect(() => {
        const token = sessionStorage.getItem('token');
        fetch("http://localhost:5000/private", {
            headers: { Authorization: 'Bearer ${token}' },         
    })
    .then(res => res.json())
    .then(data => setMessage(data.msg || "Acceso denegado"))
    .catch(err => {
        console.error(err);
        setMessage("Error al acceder a la ruta privada");
    });
    }
    , []);
    return (
        <div className="private">
            <h2>Ruta Privada</h2>
            <p>{message}</p>
        </div>
    );
};