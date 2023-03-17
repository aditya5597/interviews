import React from 'react';
import { useLocation } from 'react-router-dom';

const TaskView = (props) => {
    let location = useLocation();
    const state = location.state;
    return (
        <div>
            <h1>TaskView</h1>
            <ul>
                <li> Title : {state.task.title}</li>
                <li> Description : {state.task.description}</li>
                <li> Completed : {state.task.completed.toString()}</li>
                <li> Status : {state.task.status}</li>
            </ul>
        </div>
    );
}

export default TaskView;