import React from 'react'
import axios from 'axios'
import { useState } from 'react';

export default function CalorieTracker() {
    const [image,setImage]=useState("")
    const [food,setFood]=useState("")
    const [calorie,setCalorie]=useState("")
    const [ingridents,setIngridents]=useState("")
    function openWidget(){
      const widget = window.cloudinary.createUploadWidget(
          {
              cloudName: process.env.REACT_APP_CLOUD,
              uploadPreset: process.env.REACT_APP_PRESET,
          },
          (error, result) => {
              if (!error && result.event === "success") {
                  setImage(result.info.url)
              }
          }
      );
      widget.open();
  }
    function calculate(){
      const url = 'https://res-console.cloudinary.com/diuptzcug/thumbnails/v1/image/upload/v1710481571/MV94d3VpaWg'
      axios({
        method: "POST",
        url: "https://detect.roboflow.com/food_calorie/2",
        params: {
            api_key: "U7bCjidgxGa0MXSp4uRR",
            image
        }
    })
    .then(function(response) {
      console.log(response.data);
        let res = response.data.predictions[0].class
        setFood(res.split('-').splice(1)[0]);
        setCalorie(res.split('-').splice(1).slice(1,3));
        setIngridents(res.split('-').splice(5));
    })
    .catch(function(error) {
        console.log(error.message);
    });
    }
    return (
      <div className="App">
        <h1>Calorie Tracker</h1>
        <button onClick={openWidget} className='button'>upload</button>
        <div className="wrapper">
            <div className="image">
            {image && <img src={image} alt="image"  className='pic'/> }
            </div>
            <div className='details'>
            {food && <h2>{food}</h2>}
            <ul>
                {calorie && <li>{`${calorie[0]} in ${calorie[1]}`}</li>}
  
            </ul>
            <ul>
            {ingridents && ingridents.filter(x => x).map(i => <li>{i.trim()}</li>)}
            </ul>
            </div>
        </div>
        
        <button onClick={calculate} className='button last'>check calorie</button>
        
      </div>
    );
}
