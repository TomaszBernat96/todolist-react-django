class App extends React.Component {
    render() {
        return (
            <div>
                <h1>Hello React</h1>
                <h5>From Tomek</h5>
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('todo-app'));