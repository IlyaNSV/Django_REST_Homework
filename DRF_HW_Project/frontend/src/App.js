import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from "./components/User";
import CustomHeader from "./components/Header";
import CustomFooter from "./components/Footer";
import axios from "axios";
import {HashRouter, BrowserRouter, Link, Route, Switch, Redirect} from 'react-router-dom'
import ProjectList from "./components/Project";
import TodoNoteList from "./components/Todonote";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';


const NotFound404 = ({location}) => {
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
            'token': "",
            'header_data': 'this is testing data',
            'footer_data': 'this is testing data',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    async load_data() {
        const headers = this.get_headers()
        await axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => {
                console.log(error)
                this.setState({users: []})
            });

        await axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => {
                console.log(error)
                this.setState({projects: []})
            });

        await axios.get('http://127.0.0.1:8000/api/todonotes/', {headers})
            .then(response => {
                const todonotes = response.data.results
                this.setState(
                    {
                        'todonotes': todonotes
                    }
                )
            }).catch(error => {
                console.log(error)
                this.setState({todonotes: []})
            })
    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/'><UserList users={this.state.users}/></Route>
                        <Route exact path='/projects'><ProjectList projects={this.state.projects}/></Route>
                        <Route exact path='/todonotes'><TodoNoteList notes={this.state.todonotes}/></Route>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
                            this.get_token(username, password)}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <CustomFooter footer_data={this.state.footer_data}/>
            </div>
        )
    }
}

export default App;
