import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from "./components/User";
import CustomHeader from "./components/Header";
import CustomFooter from "./components/Footer";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'header_data': 'this is testing data',
            'footer_data': 'this is testing data',
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <CustomHeader header_data={this.state.header_data}/>
                        <UserList users={this.state.users}/>
                <CustomFooter footer_data={this.state.footer_data}/>
            </div>
        )
    }
}

export default App;
