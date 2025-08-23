'use client'

import "./layout.css"

import { Dispatch, SetStateAction, useState } from 'react';

export default function Items() {

    const [selectedItem, selectItemDescription] =
        useState(items[0].description)

    return (
        <div className="item-page">
            <div className="top-bar">
                <MenuNav />
                <PageName />
            </div>
            <div className="description-bar">
                <span>{selectedItem}</span>
            </div>
            <div className="main-view">
                <div className="character-screen"></div>
                <ItemList
                    items={items}
                    selectItemDescription={selectItemDescription}
                />
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

type ItemSelect = Dispatch<SetStateAction<string | undefined>>

type ItemListProps = {
    items: Item[];
    selectItemDescription: ItemSelect
}

type Item = {
    name: string,
    amount: number,
    selectable: boolean,
    description?: string
}



function ItemList(props: ItemListProps) {
    return (<div className="item-list">
        <ul>
            {props.items.map(x =>
                <ItemListItem
                    key={x.name}
                    selectItem={props.selectItemDescription}
                    item={x}
                />)}
        </ul>
    </div>);
}

type ItemListItemProps = {
    item: Item,
    selectItem: ItemSelect
}

function ItemListItem(props: ItemListItemProps) {
    const [amount, setAmount] = useState(props.item.amount);

    const selectable = props.item.selectable ? "selectable" : "unselectable";

    return (<li
        className={`item-list-item ${selectable}`}
        onClick={() => {
            if (props.item.selectable) {
                setAmount(amount - 1)
                props.selectItem(props.item.description)
            };
        }}
    >
        <span>{props.item.name}</span><span>:</span><span>{amount}</span>
    </li>)

}

const items: Item[] = [
    { name: "Soft", amount: 6, selectable: false, description: "Cures [Petrify]" },
    { name: "Turbo Ether", amount: 18, selectable: true, description: "Restores MP" },
    { name: "Ether", amount: 10, selectable: true },
    { name: "Phoenix Down", amount: 29, selectable: true },
    { name: "X-Potion", amount: 9, selectable: true },
    { name: "Remedy", amount: 1, selectable: false },
    { name: "Reagan Greens", amount: 3, selectable: false },
    { name: "M-Tentacles", amount: 5, selectable: false },
    { name: "Megalixir", amount: 6, selectable: true },
    { name: "Elixir", amount: 12, selectable: true },
]