import React from 'react'
import {Link} from "react-router-dom";

const MemberItem = ({member}) => {
    return (
        <tr>
            {member}
        </tr>
    )
}

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td><Link to={`project/${project.uuid}`}>{project.name}</Link></td>
            <td>{project.repository_link}</td>
            <td>{project.members.map((member) => <MemberItem member={member} />)}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Repository link
            </th>
            <th>
                Members
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList