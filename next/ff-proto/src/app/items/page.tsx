'use client'

import "./layout.css"

import { useState } from 'react';



export default function Items() {
    return (
        <div className="item-page">
            <div className="top-bar">
                <MenuNav />
                <PageName />
            </div>
            <div className="description-bar"></div>
            <div className="main-view">
                <div className="character-screen"></div>
                <ItemList items={items}/> 
            </div>
        </div>)
}

function MenuNav() {
    return (<div className="menu-nav">
        <span>Use</span>
        <span>Arrange</span>
        <span>Key Items</span>
    </div>)
}

function PageName() {
    return (
        <div className="page-name">
            <span>Item</span>
        </div>
    )
}

type ItemListProps = {
    items: Item[];
}

type Item = { name: string, amount: number, selectable: boolean }

function ItemList (props: ItemListProps) {


    return (<div className="item-list">
        <ul>
            {props.items.map(x => <ItemListItem key={x.name} {...x}/>)}
        </ul>
    </div>);
}


function ItemListItem(props: Item) {
    const [amount, setAmount] = useState(props.amount);

    const selectable = props.selectable ? "selectable" : "unselectable";

    return (<li 
                    className={`item-list-item ${selectable}`} 
                    onClick={() => {
                        if (props.selectable) setAmount(amount - 1);
                    }}
                >
                    <span>{props.name}</span><span>:</span><span>{amount}</span>
                </li>)

}

const items: Item[] = [
    { name: "Soft", amount: 6, selectable: false },
    { name: "Turbo Ether", amount: 18, selectable: true },
    { name: "Ether", amount: 10, selectable: true },
    { name: "Phoenix Down", amount: 29, selectable: true },
    { name: "X-Potion", amount: 9, selectable: true },
    { name: "Remedy", amount: 1, selectable: false },
    { name: "Reagan Greens", amount: 3, selectable: false },
    { name: "M-Tentacles", amount: 5, selectable: false },
    { name: "Megalixir", amount: 6, selectable: true },
    { name: "Elixir", amount: 12, selectable: true },
]