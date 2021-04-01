import React from 'react'
import UserList from "./User";

const CustomHeader = ({header_data}) => {
    return (
        <div>
            <h1>There could be cool header {header_data}</h1>
        </div>
    )
}

export default CustomHeader