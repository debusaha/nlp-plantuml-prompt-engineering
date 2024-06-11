import React from 'react';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            scenario: '',
            image: null,
        };
    }

    handleInputChange = (event) => {
        this.setState({
            scenario: event.target.value,
        });
    };

    handleSubmit = async (event) => {
        event.preventDefault();

        // Call your backend API here
        const response = await axios.post('http://localhost:8000/generate', {
            text: this.state.scenario,
        });

        this.setState({
            image: response.data.image_path,
        });
    };

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Scenario:
                        <input type="text" value={this.state.scenario} onChange={this.handleInputChange} />
                    </label>
                    <input type="submit" value="Generate" />
                </form>
                {this.state.image && <img src={this.state.image} alt="Generated diagram" />}
            </div>
        );
    }
}

export default App;
