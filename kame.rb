

$map = [%w(A B C D E F G H I J K),
       %w(L M N O P Q R S T U V),
       %w(W X Y Z a b c d e f g),
       %w(h i j ) + ([nil] * 5) + %w(7 6 5),
       %w(k l m ) + ([nil] * 5) + %w(4 3 2),
       %w(n o p ) + ([nil] * 5) + %w(1 0 z),
       %w(q r s ) + ([nil] * 5) + %w(y x w),
       %w(t u v ) + ([nil] * 5) + %w(v u t),
       %w(w x y ) + ([nil] * 5) + %w(s r q),
       %w(z 0 1 ) + ([nil] * 5) + %w(p o n),
       %w(2 3 4 ) + ([nil] * 5) + %w(m l k),
       %w(5 6 7 ) + ([nil] * 5) + %w(j i h),
       %w(g f e d c b a Z Y X W),
       %w(V U T S R Q P O N M L),
       %w(K J I H G F E D C B A)]

class Kame

  def exec(command)
    case command
    when /1-9a-f/
      i = command.to_i(16)
      forward(i)
    when 'R'
      R()
    when 'L'
      L()
    else
      raise 'Invalid command'
    end
  end

  def forward(i)

  end

  def L

  end

  def R

  end
end

def main
  kame = Kame.new

  command = ''
  result = ''
  command.split(//).each {|command|
    result += kame.exec(command)
  }
  puts result

end
