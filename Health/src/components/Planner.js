import React from 'react'

export default function Planner({props}) {
    const days = Object.keys(props)
  return (
    <>
        <div className='tables'>
        <table style={{"width":"500px"}}>
        <tr>
            <th>Days</th>
            <th>Excerise</th>
        </tr>
        {days.map(i => {
            return <tr>
                <td>{i}</td>
                <td>{props[i]}</td>
            </tr>
        })}
        </table>
        </div>
    </>
  )
}
