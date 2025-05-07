// src/pages/Signup.jsx
import React, { useState } from "react";

export const Signup = () => {
  const [form, setForm] = useState({ email: "", password: "" });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });
      const data = await res.json();
      alert(data.msg || "Registrado correctamente");
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Registro</h2>
      <input type="email" name="email" placeholder="Email" onChange={handleChange} />
      <input type="password" name="password" placeholder="Contraseña" onChange={handleChange} />
      <button type="submit">Registrarse</button>
    </form>
  );
};
