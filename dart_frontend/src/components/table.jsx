import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';

const Table = (props) => {
    const [tasks, setTasks] = useState(null);
    const [inedit, setInedit] = useState({
        uuid: null,
        edit: false
    });
    const [newTitle, setNewTitle] = useState(null);
    const [timeElapsed, setTimeElapsed] = useState(null);
    const startTime = new Date();
    let navigate = useNavigate();

    const handleEdit = (uuid, oldTitle) => {
        setInedit({
            uuid: uuid,
            edit: true
        });
        setNewTitle(oldTitle);
        //console.log(uuid);
    };

    const handleCancel = () => {
        setInedit({
            uuid: null,
            edit: false
        });
        setNewTitle(null);
    };

    const handleSave = () => {
        // setNewTitle(newTitle);
        console.log(newTitle);
        updateTasks();
    };

    const fetchTasks = () => {
        fetch('http://localhost:8000/api/tasks/list', {
            method: 'GET',
            mode: 'cors',
        })
            .then(res => res.json())
            .then(data => {
                setTasks(data.tasks);
            }).catch(err => {
                console.log(err);
            });
    };

    const updateTasks = () => {
        var csrftoken = Cookies.get('csrftoken');
        fetch("http://localhost:8000/api/tasks/edit", {
            method: "POST",
            credentials: "include",
            mode: "cors",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                uuid: inedit.uuid,
                newTitle: newTitle
            }),
        }).then(res => res.status === 200 ? (handleCancel(), fetchTasks()) : console.log(res.status))
            .catch(err => console.log(err));
    };

    const getTimeElapsed = () => {
        const endTime = new Date();
        var timeDiff = endTime - startTime;
        const seconds = Math.floor((timeDiff / 1000) % 60);
        const minutes = Math.floor((timeDiff / (1000 * 60)) % 60);
        const hours = Math.floor((timeDiff / (1000 * 60 * 60)) % 24);
        setTimeElapsed(`${hours}h ${minutes}m ${seconds}s`);
    };

    const handleRowClick = (task) => {
        navigate('/task', { state: { task: task } });
    };

    useEffect(() => {
        setInterval(() => {
            getTimeElapsed();
        }, 1000);
    }, []);

    useEffect(() => {
        fetchTasks();
    }, []);

    useEffect(() => {
        console.log(inedit);
        console.log(newTitle);
    }, [inedit]);

    return (
        <div className='basic-auto flex items-center'>
            <table className='table-auto divide-y divide-gray-200' >
                <thead>
                    <tr className='px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'>
                        <th>Order</th>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Completed</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody className='bg-white divide-y divide-gray-200'>
                    {tasks === null ? <tr><td>Loading...</td></tr> : Object.values(tasks).map((task) =>
                        <tr key={task.uuid} onDoubleClick={() => handleRowClick(task)}>
                            <td className='px-6 py-4 whitespace-nowrap'>{task.order}</td>
                            <td className='px-6 py-4 whitespace-nowrap' onClick={() => handleEdit(task.uuid, task.title)}>
                                {inedit.edit && inedit.uuid === task.uuid ?
                                    <span>
                                        <input className='underline underline-offset-auto' value={newTitle} onChange={(event) => setNewTitle(event.target.value)} />
                                        <button className='bg-blue-500 text-white py-1 px-2 rounded-full' onClick={handleSave} >Save</button>
                                        <button className='bg-red-500 text-white py-1 px-2 rounded-full' onClick={handleCancel} >Cancel</button>
                                    </span>
                                    : task.title}</td>
                            <td className='px-6 py-4 whitespace-nowrap'>{task.description}</td>
                            <td className='px-6 py-4 whitespace-nowrap'>{task.completed.toString()}</td>
                            <td className='px-6 py-4 whitespace-nowrap'>{task.status}</td>
                        </tr>)}
                </tbody>
            </table>
            <div className='flex-1 basic-auto text-right'>
                <button className='border-solid border-2 border-indigo-600' onClick={() => window.location.reload()}>Refresh</button>
                <p className='text-gray-600 text-sm'>Last updated: {timeElapsed}</p>
            </div>
        </div>
    );
}

export default Table;