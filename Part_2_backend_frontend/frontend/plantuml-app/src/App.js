import React from 'react';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            scenario: '',
            plantumlCode: '',
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
            plantumlCode: response.data.plantuml_code,
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
                {this.state.plantumlCode && <textarea readOnly value={this.state.plantumlCode} />}
            </div>
        );
    }
}

export default App;
