﻿Imports Discord
Imports Discord.Commands
Imports System.Reflection
Imports Discord.WebSocket
Imports System.Web
Imports Newtonsoft.Json
Imports System.Collections.ObjectModel

Module Module1

    Function drawPixelArt(input As String)
        For Each c As Char In input
            If c = "b" Then
                Console.BackgroundColor = ConsoleColor.Cyan
                Console.Write(" ")
            ElseIf c = "w" Then
                Console.BackgroundColor = ConsoleColor.White
                Console.Write(" ")
            ElseIf c = "l" Then
                Console.BackgroundColor = ConsoleColor.Black
                Console.Write(" ")
            Else
                Console.BackgroundColor = ConsoleColor.Black
                Console.ForegroundColor = ConsoleColor.Gray
                Console.Write(c)
            End If
        Next
        Console.WriteLine()
        Console.BackgroundColor = ConsoleColor.Black
        Console.ForegroundColor = ConsoleColor.Gray
    End Function

    Sub Main()
        drawPixelArt("wwwlblwww")
        drawPixelArt("wwwlblwww    BOTSTION")
        drawPixelArt("wwwlllwww    By theLMGN")
        drawPixelArt("wwwwwwwww")
        drawPixelArt("wwwwwwwww")
        Dim main = New Task(AddressOf Start)
        main.Start()
        While True
            Threading.Thread.Sleep(50000)
        End While
    End Sub

    Private WithEvents client As DiscordSocketClient

    Async Function createClient(token, name) As Task
        Await Log(New LogMessage(LogSeverity.Info, "Client", "Connecting client for " & name))
        client = New DiscordSocketClient(New DiscordSocketConfig())
        Await client.LoginAsync(TokenType.Bot, token) '" & name & "
        Await client.StartAsync
        ' Create the commands handler
        Dim commands = New CommandHandler()
        commands.Install(client, name)
    End Function

    Async Sub Start()
        Await createClient(My.Computer.FileSystem.ReadAllText("token.txt"), "Botstion")
    End Sub

    Function Log(ByVal message As LogMessage) As Task Handles client.Log
        Console.WriteLine(message.ToString())
        Return Task.CompletedTask
    End Function
End Module