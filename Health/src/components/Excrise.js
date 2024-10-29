import React, { useState } from 'react'
import axios from 'axios'
import Planner from './Planner'
import Videos from './Videos'

export default function Excrise() {
    const [links,setLinks]=useState([])
    const [name,setName] = useState("")
    const [plan,setPlan] = useState([])
    const [details,setDetails]=useState({age:"",height:"",weight:"",dance:"",weeks:""})
    const handleDetails = (e) => {
        setDetails({...details,[e.target.name]: e.target.value})
    }
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(details);
        axios.post("http://127.0.0.1:8000/", details).then((response) => {
        setPlan(response.data[0])
        setLinks(response.data[1])
    });
        
    }
  return (
    <div>
        <h1>Get your fitness plan</h1>
        <form action="" onSubmit={handleSubmit} className='details'>
            <input type="text" placeholder='name' value={name} onChange={(e) => setName(e.target.value)}/>
            <input type="text" placeholder='age' value={details.age} name="age" onChange={(e) => handleDetails(e)}/>
            <select name="" id="">
                <option value="">Gender</option>
                <option value="male">male</option>
                <option value="female">Memale</option>
            </select>
            <input type="text" placeholder='height' value={details.height} name="height" onChange={(e) => handleDetails(e)} />
            <input type="text" placeholder='weight' value={details.weight} name="weight" onChange={(e) => handleDetails(e)}/>
            <select  id="" value={details.dance} name="dance" onChange={(e) => handleDetails(e)}>
                <option value="">Do yoy like to dance</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
            <input type="text" name="weeks" id="" value={details.weeks} onChange={(e) => handleDetails(e)} placeholder='no of weeks you want' />
            <button type="submit" className='button'>Submit</button>
        </form>
       
    {plan && plan.map(p => {
            return <Planner props={p}/>
        })}
    {links.length!=0 && <h2>References</h2>}
    {links && links.map(link => {
        return <Videos props={link} />
    })}
    </div>
  )
}
