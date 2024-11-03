

-- Resize image to 1080x1080 (1:1)
function Square ()
    return "square mode"
end

-- Resize image to 1080x1350 (4:5)
function Portrait()
    print("portrait mode")
end

-- Resize image to 1080x566 (1.91:1)
function Landscape()
    print("landscape")
end

main = {}
main["square"] = Square()
main["portrait"] = Portrait
main["landscape"] = Landscape

print(main[arg[1]])