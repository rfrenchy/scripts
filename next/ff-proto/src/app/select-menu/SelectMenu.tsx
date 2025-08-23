'use client';

import "./select-menu.css"

import { AppRouterInstance } from "next/dist/shared/lib/app-router-context.shared-runtime";
import { useRouter } from "next/navigation";

// todo make menu item seperate file

export default function SelectMenu() {
    return (<div className="select-menu">
        {selectMenuData.map(x => <MenuItem
            name={x.name}
            key={x.name}
            selectable={x.selectable}
            onClick={x.onClick}
        />)}
    </div>);
}

type MenuData = {
    name: string,
    selectable: boolean,
    onClick?: (r: AppRouterInstance, selectable?: boolean) => void | (() => void)
}

function MenuItem(props: MenuData) {
    const router = useRouter();

    return (
        <div
            className={`select-menu-item ${props.selectable ? "selectable" : "not-selectable"}`}
            onClick={() => props.onClick && props.onClick(router)}
        >
            <span>{props.name}</span>
        </div>)
}

const selectMenuData: MenuData[] = [
    { name: "Item", selectable: true, onClick: (r) => r.push('/items') },
    { name: "Magic", selectable: true, onClick: (r) => r.push('/magic') },
    { name: "Materia", selectable: true, onClick: (r) => r.push('/materia') },
    { name: "Equip", selectable: true, onClick: (r) => r.push("/equip") },
    { name: "Status", selectable: true, onClick: (r) => r.push("/status") },
    { name: "Order", selectable: true, onClick: () => console.log("shuffle char image") },
    { name: "Limit", selectable: true, onClick: (r) => r.push("limit") },
    { name: "Config", selectable: true, onClick: (r) => r.push("/config") },
    { name: "PHS", selectable: false, onClick: (r, selectable) => { if (selectable) r.push("phs") } },
    { name: "Save", selectable: false, onClick: (r, selectable) => { if (selectable) r.push("save") } },
    { name: "Quit", selectable: true }
];



// make navigable 
// selected, down + up arrow navigation, detect keyboard input,
// needs focus?
// or just clickable with mouse