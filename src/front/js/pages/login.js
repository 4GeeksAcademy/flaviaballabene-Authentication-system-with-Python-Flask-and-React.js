import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
// import {useHistory} from "react-router";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const [email, SetEmail] = useState("");
	const [password, SetPassword] = useState("");
	// const history = useHistory();
	const token = sessionStorage.getItem("token");
	console.log("this is your token", store.token);

	const handleClick = () => {
		actions.login(email, password)
		
	};

	if(store.token && store.token != "" && store.token != undefined) history.pushState("/");

	return (
		<div className="text-center mt-5">
			<h1>Login</h1>
				{(store.token && store.token != "" && store.token != undefined) ? "You are logged in with this token" + store.token : 
			<div>
				<input type="text" placeholder="email" value={email} onChange={(e) => SetEmail(e.target.value)}/>
				<input type="password" placeholder="password" value={password} onChange={(e) => SetPassword(e.target.value)}/>
				<button onClick={handleClick}>Login</button>
			</div>
				}
		</div>
	);
};

// .then(() =>{
// 	history.push("/")
// })