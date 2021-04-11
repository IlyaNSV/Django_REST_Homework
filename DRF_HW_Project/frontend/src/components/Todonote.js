import React from 'react'

const NoteItem = ({note}) => {
    return (
        <tr>
            <td>{note.project}</td>
            <td>{note.creator_user}</td>
            <td>{note.text}</td>
            <td>{note.created}</td>
            <td>{note.updated}</td>
            <td>{note.actual_sign}</td>
        </tr>
    )
}

const TodoNoteList = ({notes}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Creator
            </th>
            <th>
                Text
            </th>
            <th>
                Created
            </th>
            <th>
                Updated
            </th>
            <th>
                Actuality
            </th>
            {notes.map((note) => <NoteItem note={note} />)}
        </table>
    )
}

export default TodoNoteList