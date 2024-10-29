import React from 'react'

export default function Videos({props}) {
    console.log(props);
  return (
    <>
        <div className='links'>
        {props.map(i => {
            return <>
            <a href="" src={i["links"]}>{i["links"]}</a>
            </>
        })}
        </div>
    </>
  )
}
