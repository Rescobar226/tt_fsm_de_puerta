module tt_um_Rescobar226_fsm (
    input  wire clk,
    input  wire rst_n,
    input  wire ena,
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe
);

    wire Sen = ui_in[0];
    wire SE  = ui_in[1];
    wire LA  = ui_in[2];
    wire LC  = ui_in[3];

    reg [3:0] S = 4'b0000;
    reg [3:0] S_n;

    always @(*) begin
        S_n[3] = ~S[3] & S[2] & ~S[1] & ~S[0] & ~Sen & ~SE & LA;
        S_n[2] = ~S[3] & ~S[2] & S[1] & ~S[0] & Sen & ~SE & ~LC;
        S_n[1] = (S[3] & ~S[2] & ~S[1] & ~S[0] & ~Sen & SE & ~LA & ~LC) |
                 (~S[3] & ~S[2] & ~S[1] & S[0] & Sen & ~SE & ~LA);
        S_n[0] = (S[3] & ~S[2] & ~S[1] & ~S[0] & ~Sen & ~SE & ~LA & LC) |
                 (~S[3] & ~S[2] & ~S[1] & ~S[0] & Sen & ~SE & ~LA & LC);
    end

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            S <= 4'b0000;
        else if (ena)
            S <= S_n;
    end

    wire MA = (S == 4'b0010);
    wire MC = (S == 4'b0100);

    assign uo_out[0] = MA;
    assign uo_out[1] = MC;
    assign uo_out[2] = S[0];
    assign uo_out[3] = S[1];
    assign uo_out[4] = S[2];
    assign uo_out[5] = S[3];
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    // Pines bidireccionales no usados
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
