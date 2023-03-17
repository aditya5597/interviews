import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Table from './components/table';
import TaskView from './components/TaskView';

function App() {
  return (
    <div className='container mx-auto px-4 py-2'>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Table />} />
          <Route path='/task' element={<TaskView />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App;
