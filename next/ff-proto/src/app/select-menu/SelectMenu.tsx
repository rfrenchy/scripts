'use client';

import "./select-menu.css"
import { useRouter } from "next/navigation";

// todo make menu item seperate file

export default function SelectMenu() {
    return (<div className="select-menu">
        {selectMenuData.map(x => <MenuItem name={x.name} key={x.name} selectable={x.selectable}/>)}
    </div>);
}

type MenuData = { name: string, selectable: boolean }

function MenuItem(props: MenuData) {
    const router = useRouter();

    return (
        <div 
            className={`select-menu-item ${props.selectable ? "selectable" : "not-selectable"}`} 
            onClick={() => { console.log(props.name); router.push("/items");}}    
        >
                <span>{props.name}</span>
    </div>)
}

const selectMenuData = [
    { name: "Item", selectable: true },
    { name: "Magic", selectable: true },
    { name: "Materia", selectable: true },
    { name: "Equip", selectable: true },
    { name: "Status", selectable: true },
    { name: "Order", selectable: true },
    { name: "Limit", selectable: true },
    { name: "Config", selectable: true },
    { name: "PHS", selectable: false },
    { name: "Save", selectable: false },
    {name: "Quit", selectable: true }
];



// make navigable 
// selected, down + up arrow navigation, detect keyboard input,
// needs focus?
// or just clickable with mouse