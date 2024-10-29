import React, { useEffect, useState } from 'react'
import axios  from 'axios'

export default function ChatBot() {
    const [ques,setQues] = useState({})
    const [next,setNext] = useState(["enter your age","enter your gender(M/F)","enter your problems"])
    const [curr,setCurr]=useState("")
    const [loading,setLoading] = useState(false)
    const [unload,setUnload] = useState(false)
    const [q,setQ] = useState("")
    const [c,setC] = useState(0)
    useEffect(() => {
        setQues({})
        setQues({"Greetings":"","Hello, please Enter Your Name":""})
        setCurr("Hello, please Enter Your Name")
    },[])

    const handleChat = (e) => {
        if(e.key == "Enter"){
        
            if(curr=="enter your problems"){
                setLoading(true)
                const query = {"query": q}
                console.log("ok");
                axios.post("http://127.0.0.1:8000/chat", query).then((response) => {
                       console.log(response.data);
                       setQues({
                        ...ques,
                        ...response.data
                       })
    });
    setUnload(true)
            }
            else{
            const up = {
                ...ques,
                [curr]: q
            }
            
                
                setCurr(next[c])
            
            
            const nup ={
                ...up,
                [next[c]]:""
            }
          
            setQues(nup)
            
            setC(c+1)
            
        }
        setQ("")
              
            

        }
    }
  return (
    <>
        <h1>Get Your Doubts Cleared</h1>
        <div className="over">
        {Object.keys(ques).map((v,i) => {
            return <>
            <div className="ct">{v}</div>
            {ques[v] != "" && <div className={`${v.slice(0,5)} ct`}>{ques[v]}</div>}
            </>
        })}
        {loading  &&   <div className="ct">Loading...</div> }
        </div>
        <div className='input'>
            <input type="text"
                    placeholder='Type here' 
                    className='chat-input' 
                    onKeyDown={handleChat} 
                    onChange={(e) => setQ(e.target.value)}
                    value={q}
            />
        </div>
    </>
  )
}
