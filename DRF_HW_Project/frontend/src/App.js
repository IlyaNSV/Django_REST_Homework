import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from "./components/User";
import CustomHeader from "./components/Header";
import CustomFooter from "./components/Footer";
import axios from "axios";
import {HashRouter,BrowserRouter, Link, Route, Switch, Redirect} from 'react-router-dom'
import ProjectList from "./components/Project";
import TodoNoteList from "./components/Todonote";


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todonotes': [],
            'header_data': 'this is testing data',
            'footer_data': 'this is testing data',
        }
    }

    async componentDidMount() {
        await axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error));
        await axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error));
        await axios.get('http://127.0.0.1:8000/api/todonotes/')
            .then(response => {
                const todonotes = response.data.results
                this.setState(
                    {
                        'todonotes': todonotes
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className="App">
                <CustomHeader header_data={this.state.header_data}/>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todonotes'>To do notes</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path = '/'><UserList users={this.state.users}/></Route>
                        <Route exact path = '/projects'><ProjectList projects={this.state.projects}/></Route>
                        <Route exact path = '/todonotes'><TodoNoteList notes={this.state.todonotes}/></Route>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <CustomFooter footer_data={this.state.footer_data}/>
            </div>
        )
    }
}

export default App;
